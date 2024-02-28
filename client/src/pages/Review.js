import React, { useState } from "react";
import styles from  "../styles/Review.module.css"


export const Review = () => {
  const [review, setReview] = useState("");
  const [sentiment, setSentiment] = useState("");

  const analyzeSentiment = async () => {
    const response = await fetch("http://localhost:8001/analyze-sentiment", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: review,
      }),
    });

    const data = await response.json();
    
    setSentiment(data.sentiment);
  };

  return (
    <div className={styles.main_div}>
      <label className={styles.label} htmlFor="review">
        Enter Review To Check Sentiment
      </label>
      <input
        type="text"
        value={review}
        onChange={(e) => setReview(e.target.value)}
        className={styles.input}
      />
      <button className={styles.btn} onClick={analyzeSentiment}>
        Analyze Sentiment
      </button>
      {sentiment && <p>Sentiment: {sentiment}</p>}
    </div>
  );
};
