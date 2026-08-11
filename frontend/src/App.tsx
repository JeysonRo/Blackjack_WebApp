// import { useState } from "react";
import { useQuery } from "@tanstack/react-query"
import { getGame } from "./api/game";

function App() {

  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ["game"],
    queryFn: getGame,
    enabled: false,
  });

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
          <button onClick={() => refetch()}>
            Start
          </button>
          <div>
            {isLoading && <p>WE are Loading...</p>}
            {error && <p>MFW Something went wrong.</p>}
            {data && <p>{data.message}</p>}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;