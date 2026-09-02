interface HandProps {
    cards: string[];
}

export default function Hand({ cards }: HandProps) {
    return (
        <div className="hand">
            {cards.map((card: string, index: number) => (
                <span key={index}>
                    {index > 0 && " | "}
                    {card}
                </span>
            ))}
        </div>
    )
};

// May need to consider stable id-based key instead of index