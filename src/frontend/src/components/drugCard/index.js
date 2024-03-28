import "./drug-card.css"

const DrugCard = (props) => {
    return (
        <div className="card" >
            <div className="title" style={{ backgroundColor: props.color }}>{props.status}</div> 
            <div className="content">
                <div className="drug_image">
                    <img src={props.image} className="image" alt="Foto do medicamento"/>
                </div>
                <div className="drug_info">
                    <p className="drug_name"><strong>Nome: </strong>{props.name}</p>
                    <p><strong>Dose: </strong>{props.dose}</p>
                    <p><strong>Validade: </strong>{props.expiration}</p>
                    <p> <strong>Lote: </strong>{props.batch}</p>
                    <p><strong>Fornecedor: </strong>{props.supplier}</p>
                </div>
            </div>
        </div>
    )
}

export default DrugCard;