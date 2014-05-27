var Main = (function(window, undefined){
	var _dom = {
		events:{
			click:'click',
			submit:'submit'
		},
		testForm:'#test'
	}

	function init(){
		addEventListeners();
	}

	function addEventListeners(){
		$(_dom.testForm).on(_dom.events.submit, onSubmitForm);
	}

	function onSubmitForm(event){
		if(event.preventDefault){
			event.preventDefault();
			var total = $(_dom.testForm + ' div.item').length;
			var totalSelected = $(_dom.testForm+" input:checked").length;
			if(totalSelected == total){
				console.log("complete!");
			}else{
				new Messi('Por favor, complete el formulario.', {
					title:'Mensaje',
					modal:true,
					titleClass:'error',
					buttons: [{id:0, label:'Aceptar', val:'c'}]
				});
			}
		}
	}

	return {
		init:init
	}
}(window));

Main.init();