const API="http://localhost:8000"

async function addpic(){
    const url=document.getElementById(`link`).value
    const desc=document.getElementById(`desc`).value
    const type=document.getElementById(`catype`).value
    const category=document.getElementById(`category`).value
    const msg=document.getElementById(`addmsg`)

    await fetch(`${API}/products` , {
        method:"POST",
        headers:{"Content-type":"application/json"},
        body: JSON.stringify({
            url,
            desc,
            category,
            type
        })
    });

    msg.innerText=`${desc} added successfully`

    setTimeout(() => {
        msg.innerText=''
    },3700);

}
async function get_single_cat(){
    const id=document.getElementById(`single_id`).value
    const response=await fetch( `${API}/product/${id}`)
    const cat=await response.json()
    if (response.ok) {
        document.getElementById('single_image').innerHTML = `<img src="${cat.url}" height="200px">`
        document.getElementById('single_descr').innerText = cat.desc
        document.getElementById('single_category').innerText = cat.category
        document.getElementById('single_type').innerText = cat.type
        document.getElementById(`tab`).style.display = `block`
    }else{
        document.getElementById(`yas`).innerText=cat.detail;
    }


}

async function delete_cat(){
    const id=document.getElementById('delete_id').value
    const k=document.getElementById(`dltmsg`)
    let response= await fetch( `${API}/product/${id}` ,{
        method:'DELETE'
        });
    let data=await response.json();
    if (response.ok) {
                k.innerText=data.message;
            } else {
                k.innerText='Server response:' + data.detail;
            }
}



async function update_pic(){
    const id=document.getElementById(`up_id`).value
    const url=document.getElementById(`up_link`).value
    const desc=document.getElementById(`up_desc`).value
    const type=document.getElementById(`up_catype`).value
    const category=document.getElementById(`up_category`).value
    const msg=document.getElementById(`upmsg`)
    const response=await fetch(`${API}/product/${id}`,{
        method:"PUT",
        headers:{"content-type":"application/json"},
        body:JSON.stringify(
            {
                url,
                desc,category
                ,type
            }
        )
        }

    );
    let cat= await response.json()
    msg.innerText=`Updated Details of ${cat.id} : description-> ${cat.desc} type->${cat.type} category->${cat.category}`
}



async function load_all(){
    const response= await fetch(`${API}/products`,{
        method:"get"
        });
    const data=await response.json();
    const list=document.getElementById(`products`);
    list.innerHTML="<table style=\" border: 7px solid coral\" id=\"tab\"><tr>\n" +
        "            <th>Image</th>\n" +
        "            <th>Description</th>\n" +
        "            <th>Cat Type</th>\n" +
        "            <th>Category</th>\n" +
        "        </tr>";
    data.forEach(cat=>{
        list.innerHTML+=`<tr>
            <td>${cat.url}</td>
            <td>${cat.desc}</td>
            <td>${cat.type}</td>
            <td>${cat.category}</td>
        </tr>`;
    });
    list.innerHTML+="</table>";

}
