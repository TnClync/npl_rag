import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
// import Chat from "./pages/Chat";
import Health from "./pages/Health";


export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Health />} />
        <Route path="/home" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}