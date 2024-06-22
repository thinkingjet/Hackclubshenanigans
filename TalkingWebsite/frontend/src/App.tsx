import { useState } from "react";
import Controller from "./components/Controller";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(to right, #000000, #1b1b1b, #000000)'
    }}>
      <Controller />
    </div>
  );
}

export default App;