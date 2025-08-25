import './App.css';
import { Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import logo from './octofitapp-small.png';

function App() {
  return (
    <div className="App container">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <Link className="navbar-brand text-white d-flex align-items-center" to="/">
          <img src={logo} alt="Octofit Logo" style={{height: '40px', marginRight: '10px'}} />
          Octofit Tracker
        </Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item"><Link className="nav-link text-white" to="/activities">Activities</Link></li>
            <li className="nav-item"><Link className="nav-link text-white" to="/leaderboard">Leaderboard</Link></li>
            <li className="nav-item"><Link className="nav-link text-white" to="/teams">Teams</Link></li>
            <li className="nav-item"><Link className="nav-link text-white" to="/users">Users</Link></li>
            <li className="nav-item"><Link className="nav-link text-white" to="/workouts">Workouts</Link></li>
          </ul>
        </div>
      </nav>
      <Routes>
        <Route path="/activities" element={<Activities />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/users" element={<Users />} />
        <Route path="/workouts" element={<Workouts />} />
        <Route path="/" element={
          <div className="card text-center">
            <div className="card-body">
              <h1 className="card-title">Welcome to Octofit Tracker</h1>
              <p className="card-text">Track your fitness activities, join teams, and compete on the leaderboard!</p>
            </div>
          </div>
        } />
      </Routes>
  );
    </div>
  );
}

export default App;
