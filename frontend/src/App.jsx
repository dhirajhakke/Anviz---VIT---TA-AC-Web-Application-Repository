import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("checking...");

  useEffect(() => {
    fetch("/api/health")
      .then((res) => res.json())
      .then((data) => setStatus(`${data.status} (${data.app})`))
      .catch(() => setStatus("backend unreachable"));
  }, []);

  return (
    <div style={{ fontFamily: "sans-serif", padding: "2rem" }}>
      <h1>Xthings Attendance Platform</h1>
      <p>Frontend scaffold is up.</p>
      <p>
        Backend health check: <strong>{status}</strong>
      </p>
    </div>
  );
}

export default App;
