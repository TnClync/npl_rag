import { useState } from "react";
import { queryRAG } from "../services/api";

export default function ChatBox() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input) return;

    const userMsg = { role: "user", text: input };
    setMessages([...messages, userMsg]);

    const res = await queryRAG(input);

    const botMsg = {
      role: "bot",
      text: res.answer || "No response"
    };

    setMessages(prev => [...prev, botMsg]);
    setInput("");
  };

  return (
    <div>
      <h2>RAG Chat</h2>

      <div style={{ minHeight: "200px", border: "1px solid #ccc" }}>
        {messages.map((m, i) => (
          <div key={i}>
            <b>{m.role}:</b> {m.text}
          </div>
        ))}
      </div>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask something..."
      />

      <button onClick={sendMessage}>Send</button>
    </div>
  );
}