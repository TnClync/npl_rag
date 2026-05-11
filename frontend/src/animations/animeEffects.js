import anime from "animejs";

/**
 * Fade in element
 */
export const fadeIn = (target) => {
  anime({
    targets: target,
    opacity: [0, 1],
    translateY: [20, 0],
    duration: 600,
    easing: "easeOutQuad"
  });
};

/**
 * Scale pop effect
 */
export const popIn = (target) => {
  anime({
    targets: target,
    scale: [0.9, 1],
    opacity: [0, 1],
    duration: 400,
    easing: "easeOutBack"
  });
};