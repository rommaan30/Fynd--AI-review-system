"use client";

import { useEffect, useState } from "react";

export default function AdminPage() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/admin/reviews`)
      .then((res) => res.json())
      .then(setReviews);
  }, []);

  return (
    <main style={{ padding: 40 }}>
      <h2>Admin Reviews</h2>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>ID</th>
            <th>Rating</th>
            <th>Review</th>
            <th>AI Summary</th>
            <th>AI Action</th>
          </tr>
        </thead>
        <tbody>
          {reviews.map((r) => (
            <tr key={r.id}>
              <td>{r.id}</td>
              <td>{r.rating}</td>
              <td>{r.review}</td>
              <td>{r.ai_summary}</td>
              <td>{r.ai_action}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}
