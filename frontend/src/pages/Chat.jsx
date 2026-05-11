import { useEffect, useRef, useState } from "react";
import { fadeIn, messageIn, textReveal } from "../animations/animeEffects";

export default function Chat() {
  const [messages, setMessages] = useState([
    { role: "assistant", text: "Xin chào 👋 Tôi là RAG assistant" }
  ]);

  const [input, setInput] = useState("");
  const boxRef = useRef(null);

  // 🎬 page animation
  useEffect(() => {
    fadeIn(".chat-page");
    fadeIn(".chat-input-bar");
  }, []);

  // 🎯 message animation
  useEffect(() => {
    messageIn();
  }, [messages]);

  // ✨ TEXT REVEAL cho message assistant mới nhất
  useEffect(() => {
    const lastMsg = messages[messages.length - 1];

    if (lastMsg?.role === "assistant") {
      setTimeout(() => {
        textReveal(".msg:last-child");
      }, 50);
    }
  }, [messages]);

  const sendMessage = () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", text: input };

    setMessages((prev) => [...prev, userMsg]);
    setInput("");

    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Đang xử lý RAG query..."
        }
      ]);
    }, 400);
  };

  return (
    <div className="chat-page">

      {/* CHAT BOX */}
      <div className="chat-box" ref={boxRef}>
        {messages.map((msg, idx) => (
          <div key={idx} className={`msg ${msg.role}`}>
            {/* ⚡ quan trọng: split chữ để animation */}
            {msg.text.split("").map((c, i) => (
              <span key={i}>
                {c === " " ? "\u00A0" : c}
              </span>
            ))}
          </div>
        ))}
      </div>

      {/* INPUT BAR */}
      <div className="chat-input-bar">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Nhập câu hỏi..."
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />

        <button onClick={sendMessage}>
          Send
        </button>
      </div>

    </div>
  );
}