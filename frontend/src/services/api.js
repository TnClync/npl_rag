const BASE_URL = "http://127.0.0.1:8000";

/**
 * HEALTH CHECK
 */
export async function healthCheck() {
  const res = await fetch(`${BASE_URL}/health`);
  return res.json();
}

/**
 * CHAT / RAG QUERY (chuẩn bị cho backend sau)
 */
export async function askQuestion(question) {
  const res = await fetch(`${BASE_URL}/query`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question })
  });

  return res.json();
}