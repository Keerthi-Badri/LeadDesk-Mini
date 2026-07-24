import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import API from "../services/api";

function Admin() {

  const [leads, setLeads] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetchLeads();
  }, []);


  const fetchLeads = async () => {
    try {
      const response = await API.get("/api/leads");
      setLeads(response.data);
    } catch (error) {
      console.error("Error fetching leads:", error);
    }
  };


  const updateStatus = async (id, status) => {

    try {

      await API.put(`/api/leads/${id}`, {
        status: status
      });

      fetchLeads();

    } catch (error) {
      console.error("Error updating status:", error);
    }

  };


  const filteredLeads = leads.filter((lead) =>
    lead.name.toLowerCase().includes(search.toLowerCase()) ||
    lead.email.toLowerCase().includes(search.toLowerCase())
  );

  const formatDate = (date) => {
    return new Date(date).toLocaleString("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
  };

  return (
    <div className="admin-container">

      <h1>Admin Dashboard</h1>
      <Link className="back-link" to="/">
        Back to Home
      </Link>


      <input
        className="search-box"
        type="text"
        placeholder="Search by name or email"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{
          padding: "10px",
          width: "300px",
          marginBottom: "20px"
        }}
      />


      <table border="1" cellPadding="10">

        <thead>

          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Budget</th>
            <th>Message</th>
            <th>Status</th>
            <th>Date</th>
          </tr>

        </thead>


        <tbody>

          {
            filteredLeads.map((lead) => (

              <tr key={lead.id}>

                <td>{lead.name}</td>

                <td>{lead.email}</td>

                <td>{lead.budget}</td>

                <td>{lead.message}</td>

                <td>

                  <select
                    value={`status-${lead.status.toLowerCase()}`}
                    value={lead.status}
                    onChange={(e) =>
                      updateStatus(
                        lead.id,
                        e.target.value
                      )
                    }
                  >

                    <option>New</option>
                    <option>Contacted</option>
                    <option>Closed</option>

                  </select>

                </td>

                <td>
                  {formatDate(lead.created_at)}
                </td>

              </tr>

            ))
          }


        </tbody>


      </table>


    </div>
  );
}


export default Admin;