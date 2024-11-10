/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#00a3ae",
        bg: "#f5f5f5",
        graytext: "#939393",
        navbg: "#fafafa"
      },
    },
  },
  plugins: [],
}