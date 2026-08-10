import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  async function startGame() {
    const response = await fetch("/api/game");
    const data = await response.json();

    setMessage(data.message);
  }
  return (
    <div className="App">
      <header>
        <h1>Blackjack</h1>
      </header>

      <main>
        <section className="dealer">
          <h2>Dealer</h2>
          <div className="hand">
            {/* Dealer cards */}
          </div>
        </section>

        <div className="actions">
          <button>Hit</button>
          <button>Stand</button>
          <button>Double Down</button>
          <button>Split</button>
        </div>
        <div className="Menu">
          <button onClick={startGame}>
            Start
          </button>
          <p>{message}</p>
        </div>
      </main>
    </div>
  );
}

export default App;