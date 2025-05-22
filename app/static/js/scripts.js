document.addEventListener("DOMContentLoaded", () => {
    let currentPage = 1;
    let rowsPerPage = 5;
    let totalPages = 1;
    
    const tbody = document.getElementById('tableBody');
    const selectRows = document.getElementById('rowsCount');
    const paginationDiv = document.getElementById('paginationControls');
    
    function displayTable() {
        const startIdx = (currentPage - 1) * rowsPerPage;
        const endIdx = startIdx + rowsPerPage;
        const pageData = data.slice(startIdx,endIdx);
    
        tbody.innerHTML = '';
        for(const item of pageData){
            const row = document.createElement('tr');
    
            row.innerHTML = `
                    <td>${item.id}</td>
                    <td><img src="${item.picture}" alt="Фото" class="photo"></td>
                    <td>${item.gender}</td>
                    <td>${item.first_name}</td>
                    <td>${item.last_name}</td>
                    <td>${item.phone}</td>
                    <td>${item.email}</td>
                    <td>${item.location}</td>
                    <td><a href="/users/${item.id}" class="action-btn">Подробнее</a></td>
                `;
            tbody.appendChild(row);
        }
    }
    function updatePagination() {
        totalPages = Math.ceil(data.length / rowsPerPage);
        paginationDiv.innerHTML = '';
    
        const prevBtn = document.createElement('button');
        prevBtn.textContent='Предыдущая';
        prevBtn.className='page-btn';
        prevBtn.disabled = currentPage === 1 ;
        prevBtn.onclick = () => { if(currentPage > 1){ currentPage--; displayTable(); updatePagination(); } };
        paginationDiv.appendChild(prevBtn);
    
        for (let i = 1; i <= totalPages; i++) {
            if (Math.abs(i - currentPage) >= 5 && i !== totalPages && i !== 1) { continue; }
            const pageBtn = document.createElement('button');
            pageBtn.textContent = i.toString();
            pageBtn.className = 'page-btn';
            if (i === currentPage) { pageBtn.disabled = true;}
            pageBtn.onclick = () => { currentPage = i; displayTable(); updatePagination(); };
            if (totalPages - currentPage > 5 && i === totalPages) {
                const points = document.createElement('p');
                points.textContent = '...'
                paginationDiv.appendChild(points);
            }
            paginationDiv.appendChild(pageBtn);
            if (currentPage > 6 && i === 1) {
                const points = document.createElement('p');
                points.textContent = '...'
                paginationDiv.appendChild(points);
            }
        }
    
        const nextBtn = document.createElement('button');
        nextBtn.textContent='Следующая';
        nextBtn.className='page-btn';
        nextBtn.disabled= currentPage===totalPages ;
        nextBtn.onclick = () => { if (currentPage < totalPages){ currentPage++; displayTable(); updatePagination(); } };
        paginationDiv.appendChild(nextBtn);
    }
    
    selectRows.addEventListener('change',(e)=>{
        const val = e.target.value;
        if(val==='все'){
            rowsPerPage = data.length;
        } else {
            rowsPerPage = parseInt(val);
        }
        currentPage=1;
        displayTable();
        updatePagination();
    });
    
    rowsPerPage=parseInt(selectRows.value);
    displayTable();
    updatePagination();

});