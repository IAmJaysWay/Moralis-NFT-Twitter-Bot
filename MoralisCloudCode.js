//Send tokenID, price and raw image data of
//synced CryptoPunk sale events

Moralis.Cloud.afterSave("Punks", async (request) =>{
  
  const name = request.object.get('punkIndex')
  const value = Number(request.object.get('value'))/1000000000000000000
  
  const options = { 
	address: "0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb", 
	token_id: name
  }

  const tokenIdMetadata = await Moralis.Web3API.token.getTokenIdMetadata(options);
  
  const metadata = JSON.parse(tokenIdMetadata.metadata)
  const image = metadata.image
  
  Moralis.Cloud.httpRequest({
  	url: image
  }).then(function(httpResponse) {
    
    Moralis.Cloud.httpRequest({
  		method: 'POST',
  		url: '<server URL>',
  		headers: {
    		'Content-Type': 'application/json'
  		},
  		body: {
    		'name': name,
   		 	'price': value,
   		 	'content' : httpResponse.buffer
  		}
  	})	
    
    
  })
})
