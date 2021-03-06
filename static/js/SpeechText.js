var SpeechText = function(bid, langCd, idToSpeak) {

	this.msg = ('speechSynthesis' in window) ? new SpeechSynthesisUtterance() : null;
	this.intDivide = (localStorage.getItem(bid)) ? localStorage.getItem(bid)-2 : 0;
	if ('speechSynthesis' in window) {
	    this.msg.lang = (langCd)? langCd : "en-US";
	    // this.msg.pitch = 1.8;
	}

	var t = document.createElement('div');
	t = document.getElementById(idToSpeak).innerText + ".";
	this.arrText = (t.replace(/\n\n/gi, '        ').replace(/ \n/gi, '').replace(/\n/gi, '').replace(/\./gi, '\. ').replace(/,/gi, ', ')).split(". ");
	this.boardid = bid;

	this.divideText = function() {
		var t = "";
		if (this.intDivide<this.arrText.length-1) t = this.arrText[this.intDivide++] + ". ";
		localStorage.setItem(this.boardid, this.intDivide);
		return t;
	};

	this.start = function() {
		this.intDivide = 0;
		this.speak();
	};

	this.keepon = function() {
		this.speak();
	};

	/* speak */
	this.speak = function() {
		if ('speechSynthesis' in window) { // ie11 x, chrome o, safari o
			this.msg.text = this.divideText();
			if (this.msg.text!="") window.speechSynthesis.speak(this.msg);
		}
	};

	this.stop = function() {
		if ('speechSynthesis' in window) {
			localStorage.setItem(this.boardid, this.intDivide);
			window.speechSynthesis.cancel();
		}
	};
}