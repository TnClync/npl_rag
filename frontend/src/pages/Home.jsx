import { Link } from "react-router-dom";

import { useEffect } from "react";
import { fadeIn, popIn } from "../animations/animeEffects";

export default function Home() {
  useEffect(() => {
    popIn(".title");
  }, []);
  
  return (
    <div className="home">
      <h1 className="title">RAG Chat App</h1>
    </div>
  );
}