import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import Footer from "./components/Footer";
import IDForm from "./components/forms/IDForm";
import Main from "./pages/Main";
import RiskForm from "./components/forms/riskForm";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <BrowserRouter>
        <main>
          <div>
            <a href="https://vite.dev" target="_blank">
              <img src={viteLogo} className="logo" alt="Vite logo" />
            </a>
            <a href="https://react.dev" target="_blank">
              <img src={reactLogo} className="logo react" alt="React logo" />
            </a>
          </div>
          <h1>Vite + React</h1>
          <div className="card">
            <button onClick={() => setCount((count) => count + 1)}>
              Count is {count}
            </button>
            <p>
              Edit <code>src/App.tsx</code> and save to test HMR
            </p>
            <p className="read-the-docs">
              Click on the Vite and React logos to learn more
            </p>
          </div>
          <div className="route-to-favorites">
            <Routes>
              <Route path="/" element={<RiskForm />}></Route>
              {/* <Route
                path="/favorites/:username"
                element={<Main username={username} />}
              /> */}
            </Routes>
          </div>
        </main>
      </BrowserRouter>
      <Footer />
    </>
  );
}

export default App;
