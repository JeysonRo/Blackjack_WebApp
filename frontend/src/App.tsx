// import { useState } from "react";
import { useQuery, useMutation } from "@tanstack/react-query"
import { getGame, startGame } from "./api/game";
import "./App.css"
import Actions from "./components/Actions"
import Menu from "./components/Menu";

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
        
        <Actions startGameMutation={startGameMutation} /> {/* Component for displaying available actions */}
        

        <div className="GetInfo">
          <button onClick={() => gameQuery.refetch()}>
            GetInfo
          </button>
            <div>
              {gameQuery.isLoading && <p>WE are Loading...</p>}
              {gameQuery.error && <p>MFW Something went wrong.</p>}
              {gameQuery.data && <p>{gameQuery.data.message}</p>}
            </div>
          </div>

        <Menu startGameMutation={startGameMutation} /> {/* Component for displaying Menu */}

      </main>
    </div>
  );
}

export default App;