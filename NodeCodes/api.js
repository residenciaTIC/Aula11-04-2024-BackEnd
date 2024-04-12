const path = "http://127.0.0.1:3000"

fetch(path)
    .then((response) => response.json())
    .then((data) => {
        document.getElementById('projeto').innerText = data.projeto
        document.getElementById('alunos').innerText = data.nroAlunos
        document.getElementById('turma').innerText = data.turma
    }
    )