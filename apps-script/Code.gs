const CONFIG = {
  documentId: 'DOC_ID',
  secret: 'SYNC_SECRET',
  allowEmpty: 'ALLOW_EMPTY',
  lastSyncAt: 'LAST_SYNC_AT',
  lastSyncChars: 'LAST_SYNC_CHARS',
};

function doGet() {
  return jsonResponse_({
    ok: true,
    service: 'daily-news-briefing-doc-sync',
  });
}

function doPost(e) {
  try {
    return jsonResponse_(syncMarkdownToDoc_(e));
  } catch (error) {
    return jsonResponse_({
      ok: false,
      error: String(error && error.message ? error.message : error),
    });
  }
}

function syncMarkdownToDoc_(e) {
  const payload = parseJsonPayload_(e);
  const props = PropertiesService.getScriptProperties();
  const documentId = props.getProperty(CONFIG.documentId);
  const expectedSecret = props.getProperty(CONFIG.secret);

  if (!documentId) {
    throw new Error('Missing script property: DOC_ID');
  }
  if (!expectedSecret) {
    throw new Error('Missing script property: SYNC_SECRET');
  }
  if (!payload.secret || payload.secret !== expectedSecret) {
    throw new Error('Invalid secret');
  }
  const markdown = typeof payload.markdown === 'string' ? payload.markdown : payload.text;

  if (typeof markdown !== 'string') {
    throw new Error('Request JSON must include markdown or text as a string');
  }
  if (markdown.trim() === '' && props.getProperty(CONFIG.allowEmpty) !== 'true') {
    throw new Error('Refusing to replace the document with empty markdown');
  }

  const lock = LockService.getScriptLock();
  lock.waitLock(30000);

  try {
    const doc = DocumentApp.openById(documentId);
    doc.getBody().setText(markdown);
    doc.saveAndClose();

    const updatedAt = new Date().toISOString();
    props.setProperty(CONFIG.lastSyncAt, updatedAt);
    props.setProperty(CONFIG.lastSyncChars, String(markdown.length));

    return {
      ok: true,
      documentId,
      updatedAt,
      characters: markdown.length,
    };
  } finally {
    lock.releaseLock();
  }
}

function parseJsonPayload_(e) {
  if (!e || !e.postData || !e.postData.contents) {
    throw new Error('Missing POST body');
  }

  try {
    return JSON.parse(e.postData.contents);
  } catch (error) {
    throw new Error('POST body must be valid JSON');
  }
}

function jsonResponse_(payload) {
  return ContentService
    .createTextOutput(JSON.stringify(payload))
    .setMimeType(ContentService.MimeType.JSON);
}
