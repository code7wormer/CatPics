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
        msg.innertext=''
    },3700);

}
async function get_single_cat(){
    const id=document.getElementById(`single_id`).value
    const response=await fetch( `${API}/product/${id}`)
    const cat=await response.json()
    document.getElementById('single_image').innerHTML=`<img src="${cat.url}" height="200px">`
    document.getElementById('single_descr').innerText=cat.desc
    document.getElementById('single_category').innerText=cat.category
    document.getElementById('single_type').innerText=cat.type
    document.getElementById(`tab`).style.display=`block`


}