import React from 'react'
// import {reaction} from 'mobx'
import {observer} from 'mobx-react'
import {Line} from 'react-konva'
import {getColor} from 'app/utils'


@observer
class Street extends React.Component {
	disposer;
	line;

	// constructor(props) {
	// 	super(props);
	// 	this.disposer = reaction(
	// 		() => this.props.street.percent,
	// 		this.updateColor
	// 	)
	// }

	// updateColor = (percent) => {
	// 	console.log('updating color', getColor(percent), this.line);
	// 	this.line.fill(getColor(percent));
	// 	this.line.draw();
	// };
	//
	// lineRef = (el) => {
	// 	if (!this.line) {
	// 		this.line = el;
	// 	}
	// };
	//
	// shouldComponentUpdate() {
	// 	return false;
	// }

	render() {
		const {from, to, percent} = this.props.street;

		return (
			<Line
				stroke={getColor(percent)}
				strokeWidth={3}
				points={[from.x, from.y, to.x, to.y]}
				ref={this.lineRef}
			/>
		)
	}
}

export default Street