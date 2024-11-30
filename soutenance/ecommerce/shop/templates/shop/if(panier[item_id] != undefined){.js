if(panier[item_id] != undefined){
                quantite= panier[item_id][0] +1 ;
                panier[item_id][0] = quantite;
            }else{
                quantite = 1;
                nom = document.getElementById("aa" + item_id).innerHTML;
                panier[item_id]=[quantite,nom];
            }
            console.log(panier);
            localStorage.setItem('panier',JSON.stringify(panier));
            document.getElementById("panier").innerHTML = "Panier("+Object.keys(panier).length+")";
            panierString+=document.getElementById("aa" +x).innerHTML + " Quantite: " + panier[x] + "</br>";