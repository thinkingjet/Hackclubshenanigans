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


// Documentation:
// The App component serves as the root component for the application, providing a foundation upon which other components are built. In this code, the App component is primarily responsible for rendering the Controller component, which manages the core functionality of the application.

// State Management: Although the count state and its corresponding setCount function are defined, they are not used in the current implementation. This might indicate potential future functionality where the state could be utilized.
// Styling: The App component applies a full-height background style with a dark gradient, enhancing the visual aesthetics and providing a sleek, modern look that aligns with the high-tech theme of a Tesla AI Sales Rep.
// Component Hierarchy: The Controller component, imported at the top, is embedded within the App component. This makes Controller a child of App, signifying that all the main interactive elements and functionalities (such as audio recording and message handling) are managed by the Controller.