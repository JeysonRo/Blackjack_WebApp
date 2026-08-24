// import { useState } from "react";
import { useQuery, useMutation } from "@tanstack/react-query"
import { getGame, startGame } from "./api/game";
import "./App.css"

function App() {

  const gameQuery = useQuery({
    queryKey: ["game"],
    queryFn: getGame,
    enabled: false,
  });

  const startGameMutation = useMutation({
    mutationFn: startGame,
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
          <button onClick={() => gameQuery.refetch()}>
            GetInfo
          </button>
          <div>
            {gameQuery.isLoading && <p>WE are Loading...</p>}
            {gameQuery.error && <p>MFW Something went wrong.</p>}
            {gameQuery.data && <p>{gameQuery.data.message}</p>}
          </div>
          </div>
        <div className="Menu">
          <button
           onClick={() => startGameMutation.mutate()}
           disabled={startGameMutation.isPending}
           >
            {startGameMutation.isPending ? "Starting..." : "Start Game"}
          </button>

          {startGameMutation.isError && (
            <p>Error: {startGameMutation.error.message}</p>
          )}

          {startGameMutation.data && (
            <div>
              {startGameMutation.data.player_hand.map((card: string, index: number) => (
                <span key={index}>
                  {index > 0 && " | "}
                  {card}
                </span>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;