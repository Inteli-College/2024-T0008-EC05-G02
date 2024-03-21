const DrugCard = (props) => {
    const { drug } = props;
    return (
        <div className="card" >
            <div className="title" style={{ backgroundColor: drug.color }}>{drug.status}</div> 
            <div className="content">
                <div className="drug_image">
                    <img src={drug.image} className="image" alt="Foto do medicamento"/>
                </div>
                <div className="drug_info">
                    <p className="drug_name"><strong>Nome: </strong>{drug.name}</p>
                    <p><strong>Dose: </strong>{drug.dose}</p>
                    <p><strong>Validade: </strong>{drug.expiration}</p>
                    <p> <strong>Lote: </strong>{drug.batch}</p>
                    <p><strong>Fornecedor: </strong>{drug.supplier}</p>
                </div>
            </div>
        </div>
    )
}

export default DrugCard;