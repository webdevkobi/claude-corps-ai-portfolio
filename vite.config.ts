import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig(({ command }) => ({
  base: command === "build" ? "/claude-corps-ai-portfolio/" : "/",
  plugins: [react()],
}));
