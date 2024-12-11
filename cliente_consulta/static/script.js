async function buscaCliente() {
    const doc_cpf = document.getElementById('cpf').value;
    console.log(doc_cpf)
    if (!doc_cpf){
        alert('Por favor, insira um CPF');
        return;
    }
    // devemos tratar erros
    const response = await fetch(`http://127.0.0.1:5000/consulta?doc=${doc_cpf}`)
    
    const dados = await response.json();
    console.log(dados)
    document.getElementById('nome').textContent = dados.nome;
    document.getElementById('nasc').textContent = dados.data_nascimento;
    document.getElementById('email').textContent = dados.email;
}

async function cadastrar_cliente() {
    const cpf = document.getElementById("cpf-c").value
    const nome = document.getElementById("nome-c").value
    const data_nascimento = document.getElementById("nasc-c").value
    const email = document.getElementById("email-c").value
    //criar a estrutura que definimos pro json
    const payload = {
        cpf,
        dados: {
            nome,
            data_nascimento,
            email
        }
    }

    //fazer a requisição no backend
    const response = await fetch("http://127.0.0.1:5000/cadastro", {
        method: "post",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)

    })
    const retorno = await response.json()

    if (retorno){
        alert("usuário já cadastrado.")
    }else{
        alert("Cadastro realizado.")
    }

}