import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Foreman from "./Pages/Foreman";
import Project_Manager from "./Pages/Project_Manager";
import General_Manager from "./Pages/General_Manager";
import Jobs from "./Pages/Jobs";
import Home from "./Pages/Home";
import Inventory from "./Pages/Inventory";
import Electricians from "./Pages/Electricians";

function App() {

  return (
      <div className="App container m-4">
      <div className="row">
      <div className="text-center">
      <Router>
      <div>
        <Link to="/">Home</Link>
      </div>
      <div>
        <Link to="/jobs">Jobs</Link>
      </div>
      <div>
        <Link to="/inventory">Inventory</Link>
      </div>
      <div>
        <Link to="/electricians">Electricians</Link>
      </div>
      <div>
        <Link to="/general_manager">General Managers</Link>
      </div>
      <div>
        <Link to="/project_manager">Project Managers</Link>
      </div>
      <div>
        <Link to="/foreman">Foremen</Link>
      </div>

      <hr />

      <Routes>
      <Route path="/" element={<Home />}>
        </Route>
        <Route path="/jobs" element={<Jobs />}>
        </Route>
        <Route path="/inventory" element={<Inventory />}>
        </Route>
        <Route path="/electricians" element={<Electricians />}>
        </Route>
        <Route path="/general_manager" element={<General_Manager />}>
        </Route>
        <Route path="/project_manager" element={<Project_Manager />}>
        </Route>
        <Route path="/foreman" element={<Foreman />}>
        </Route>
      </Routes>
    </Router>
        </div>
        </div>

         </div>

  );
}


export default App;
