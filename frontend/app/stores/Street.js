import {observable, action} from 'mobx'


export class Street {
	id;
	from;
	to;
	@observable percent;

	constructor(props) {
		this.setInitial(props);
	}

	@action.bound setInitial(props) {
		Object.assign(this, props);
	}

	@action.bound update(props) {
		this.percent = props.percent;
	}
}