"use client";

import { useState } from "react";

export default function Home() {
  const [rating, setRating] = useState(5);
  const [review, setReview] = useState("");
  const [message, setMessage] = useState("");

  const submitReview = async () => {
    setMessage("");

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/reviews`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ rating, review }),
        }
      );

      if (!res.ok) throw new Error("Submission failed");

      setMessage(" Review submitted successfully");
      setReview("");
    } catch (err) {
      setMessage("Failed to submit review");
    }
  };

  return (
    <main style={{ padding: 40 }}>
      <h2>User Review</h2>

      <select
        value={rating}
        onChange={(e) => setRating(Number(e.target.value))}
      >
        {[1, 2, 3, 4, 5].map((r) => (
          <option key={r} value={r}>
            {r}
          </option>
        ))}
      </select>

      <br /><br />

      <textarea
        rows={4}
        cols={40}
        placeholder="Write your review..."
        value={review}
        onChange={(e) => setReview(e.target.value)}
      />

      <br /><br />

      <button onClick={submitReview}>Submit</button>

      <p>{message}</p>
    </main>
  );
}
