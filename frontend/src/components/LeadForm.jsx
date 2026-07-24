import { useState } from "react";
import API from "../services/api";

function LeadForm() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    budget: "",
    message: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Client-side validation
    if (
      !formData.name ||
      !formData.email ||
      !formData.budget ||
      !formData.message
    ) {
      alert("Please fill all fields.");
      return;
    }

    try {
      const response = await API.post("/api/leads", formData);

      alert(response.data.message);

      setFormData({
        name: "",
        email: "",
        budget: "",
        message: "",
      });
    } catch (error) {
      alert(
        error.response?.data?.error || "Something went wrong."
      );
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="name"
        placeholder="Full Name"
        value={formData.name}
        onChange={handleChange}
      />

      <input
        type="email"
        name="email"
        placeholder="Email Address"
        value={formData.email}
        onChange={handleChange}
      />

      <select
        name="budget"
        value={formData.budget}
        onChange={handleChange}
      >
        <option value="">Select Budget</option>
        <option value="Under 50,000">Under 50,000</option>
        <option value="50,000 - 1,00,000">50,000 - 1,00,000</option>
        <option value="Above 1,00,000">Above 1,00,000</option>
      </select>

      <textarea
        name="message"
        rows="5"
        placeholder="Tell us about your project"
        value={formData.message}
        onChange={handleChange}
      ></textarea>

      <button type="submit">Submit Lead</button>
    </form>
  );
}

export default LeadForm;