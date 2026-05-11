import { useEffect, useState } from "react";
import { healthCheck } from "../services/api";
import { fadeIn } from "../animations/animeEffects";

export default function Health() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const checkHealth = async () => {
    try {
      setLoading(true);
      setError("");
      setData(null);

      const res = await healthCheck();
      setData(res);
    } catch (err) {
      setError("Cannot connect to backend ❌");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fadeIn(".health-card");
  }, []);

  const isHealthy = data?.status === "ok";

  return (
    <div className="health-page">
      <div className="health-card">

        <div className="header">
          <h1>🩺 API Health Dashboard</h1>
          <span className={`status ${isHealthy ? "ok" : "bad"}`}>
            {data ? (isHealthy ? "ONLINE" : "ERROR") : "UNKNOWN"}
          </span>
        </div>

        <p className="subtitle">FastAPI system monitoring</p>

        <button onClick={checkHealth}>
          Check API
        </button>

        {loading && <p className="loading">Checking backend...</p>}
        {error && <p className="error">{error}</p>}

        {data && (
          <div className="info-box">
            <div className="row">
              <span>Status:</span>
              <b>{data.status}</b>
            </div>

            <div className="row">
              <span>Message:</span>
              <b>{data.message}</b>
            </div>

            <div className="row">
              <span>Time:</span>
              <b>{new Date(data.timestamp).toLocaleString()}</b>
            </div>
          </div>
        )}

      </div>
    </div>
  );
}