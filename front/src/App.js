import  {useEffect} from 'react';
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";



import Landing from "./views/landing.js";

function App() {

  useEffect(()=>{
    document.title = "Note Taking APP";
  },[]);

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Landing />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
