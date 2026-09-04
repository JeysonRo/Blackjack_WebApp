const cardImages = import.meta.glob(
    "../assets/cardArt/*.svg",
    { eager: true, query: "?url", import: "default"}
) as Record<string, string>;

function getCardImage(card: string) {
    if (card == "hidden" || card == "Hidden") {
        return cardImages[`../assets/cardArt/card_back.svg`];
    }
    card = card.toLowerCase()
    return cardImages[`../assets/cardArt/${card}.svg`];
}

interface HandProps {
    cards: string[];
}

export default function Hand({ cards }: HandProps) {
    return (
        <div className="hand">
            {cards.map((card: string, index: number) => (
                <img 
                    key={index}
                    src={getCardImage(card)}
                    alt={card}/>
            ))}
        </div>
    )
};

// May need to consider stable id-based key instead of index