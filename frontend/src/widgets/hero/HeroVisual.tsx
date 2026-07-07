// Hero Right Panel: visual elements
// Placeholder for visual elements
// TODO: Add visual elements here
export const HeroVisual = () => {
    return (
      // <div
      //   className="
      //     flex min-h-[280px] w-full items-center justify-center
      //     rounded-2xl border border-dashed border-border-secondary
      //     bg-background-secondary/40
      //     lg:min-h-[420px]
      //   "
      //   aria-hidden="true"
      // >
      //   <p className="font-body text-sm text-text-muted">
      //     Visual coming soon
      //   </p>
      // </div>
      <FigureEightVisual className="px-4 py-2"/>
    );
  };

import { useRef, useEffect } from 'react';

/**
 * Calculates the x and y coordinates for a given angle
 * in the Lemniscate of Bernoulli curve
 * @param a - The angle in radians (0 to 2π)
 * @param r - The radius of the curve (controls overall size of the curve)
 * @param cx - The x coordinate of the center of the canvas
 * @param cy - The y coordinate of the center of the canvas
 * @returns The x and y coordinates of the point on the canvas for that angle
 */
function lemniscatePoint(a: number, r: number, cx: number, cy: number) {

  const denominator = 1 + Math.sin(a)* Math.sin(a)
  const x = cx + (r * Math.sin(a) * Math.cos(a)) / denominator
  const y = cy + (r * Math.cos(a)) / denominator
  return { x, y }
}

const RING_AS_RATIO = [
  { baseRatio: 0.13, ampRatio: 0.018, speed: 1.00, alpha: 0.80, linewidth: 2.5, dash: [] as number[] },
  { baseRatio: 0.22, ampRatio: 0.028, speed: 0.75, alpha: 0.38, linewidth: 2.0, dash: [3, 7]         },
  { baseRatio: 0.31, ampRatio: 0.035, speed: 0.55, alpha: 0.20, linewidth: 1.8, dash: [] as number[] },
  { baseRatio: 0.40, ampRatio: 0.033, speed: 0.40, alpha: 0.12, linewidth: 1.6, dash: [2, 9]         },
  { baseRatio: 0.50, ampRatio: 0.023, speed: 0.28, alpha: 0.06, linewidth: 1.4, dash: [] as number[] },
];
function getRingsFromRatios(scale: number) {
  return RING_AS_RATIO.map((ring) => {
    return {
      base: ring.baseRatio * scale,
      amplitude: ring.ampRatio * scale,
      speed: ring.speed,
      alpha: ring.alpha,
      linewidth: ring.linewidth,
      dash: ring.dash,
    }
  })
};

function measure(wrapper: HTMLElement, canvas: HTMLCanvasElement) {
  const WIDTH = wrapper.clientWidth;
  const HEIGHT = wrapper.clientHeight;
  
  canvas.width = WIDTH;
  canvas.height = HEIGHT;

  const CENTER_X = WIDTH / 2;
  const CENTER_Y = HEIGHT / 2;

  const scale = Math.min(WIDTH, HEIGHT);

  const rings = getRingsFromRatios(scale);

  return { WIDTH, HEIGHT, CENTER_X, CENTER_Y, rings };
}

function FigureEightVisual() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const wrapperRef = useRef<HTMLDivElement>(null);
  // const cursorRef = useRef({x: 0, y: 0, inside: false});

  useEffect(() => {
    const canvas = canvasRef.current;
    const wrapper = wrapperRef.current;
    if (!canvas || !wrapper) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Get the geometry of the canvas based on the wrapper size
    let geometry = measure(wrapper, canvas);

    // TODO: Add mouse tracking

    let t = 0;
    let animationId: number;
    const DOT_COUNT = 32;

    function draw() {
      const { WIDTH, HEIGHT, CENTER_X, CENTER_Y, rings } = geometry;
      ctx.clearRect(0, 0, WIDTH, HEIGHT);

      // Draw the lemniscate rings
      rings.forEach((ring, i) => {
        // Breathing effect: radius oscillates between base and base + amplitude at a rate of speed with per-ring phase offset
        const radius = ring.base + ring.amplitude * Math.sin(t * ring.speed + i * Math.PI * 0.4);
        
        ctx.beginPath();

        const STEPS = 360;
        for (let step = 0; step < STEPS; step++) {
          const angle = (step / STEPS) * 2 * Math.PI;
          const point = lemniscatePoint(angle, radius, CENTER_X, CENTER_Y);
          step === 0 ? ctx.moveTo(point.x, point.y) : ctx.lineTo(point.x, point.y);
        }
        ctx.closePath();

        ctx.strokeStyle = `rgba(232,214,182, ${ring.alpha})`;
        ctx.lineWidth = ring.linewidth;
        ctx.setLineDash(ring.dash);
        ctx.stroke();
        ctx.setLineDash([]);
      });

      // Draw the orbiting dots
      const DOTS_RADIUS = rings[1].base + rings[1].amplitude * Math.sin(t * rings[1].speed);
      for (let d = 0; d < DOT_COUNT; d++) {
        const angle = (d / DOT_COUNT) * 2 * Math.PI + t * 0.05;
        const point = lemniscatePoint(angle, DOTS_RADIUS, CENTER_X, CENTER_Y);
        const pulse = 0.2 + 0.45 * Math.sin(t * 2 + d * 0.8);

        ctx.beginPath();
        ctx.arc(point.x, point.y, 2, 0, 2 * Math.PI);
        ctx.fillStyle = `rgba(232,214,182, ${pulse})`;
        ctx.fill();
        ctx.closePath();
      }

      // Center dot
      ctx.beginPath();
      ctx.arc(CENTER_X, CENTER_Y, 4, 0, 2 * Math.PI);
      ctx.fillStyle = `rgba(232,214,182, 0.7)`;
      ctx.fill();
      ctx.closePath();

      ctx.beginPath();
      ctx.arc(CENTER_X, CENTER_Y, 2, 0, 2 * Math.PI);
      ctx.fillStyle = `rgba(232,214,182, 1)`;
      ctx.fill();
      ctx.closePath();

      const TICK = 0.018;
      t += TICK;
      animationId = requestAnimationFrame(draw);
    }
    const resizeObserver = new ResizeObserver(() => {
      geometry = measure(wrapper, canvas);
    });
    resizeObserver.observe(wrapper);
    draw();

    return () => {
      if (animationId) cancelAnimationFrame(animationId);
      resizeObserver.disconnect();
    };
  }, []);

  return (
    <div ref={wrapperRef} className="w-full h-full flex items-center justify-center">
      <canvas
        ref={canvasRef}
        className="block"
      />
    </div>
  );
}