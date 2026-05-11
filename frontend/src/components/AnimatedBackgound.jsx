import { useEffect } from "react";
import { initAnimation } from "../src/animations/animeEffects";

export default function AnimatedBackground() {
  useEffect(() => {
    initAnimation();
  }, []);

  return <div className="background" />;
}