import {observable, action} from 'mobx'


export class Intersection {
	id;
	x;
	y;
	streets;
	@observable open;

	constructor(props) {
		this.setInitial(props);
	}

	@action.bound setInitial(props) {
		Object.assign(this, props);
	}

	@action.bound update(props) {
		this.open = props.open;
	}
}