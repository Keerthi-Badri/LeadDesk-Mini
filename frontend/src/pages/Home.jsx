import LeadForm from "../components/LeadForm";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="container">

      <nav>
        <Link to="/admin">
          Admin Dashboard
        </Link>
      </nav>


      <h1>LeadDesk Mini</h1>

      <p className="subtitle">
        Capture and manage your business leads efficiently.
      </p>

      <LeadForm />


      <footer>
        Built for Digital Heroes Training Task
      </footer>

    </div>
  );
}

export default Home;