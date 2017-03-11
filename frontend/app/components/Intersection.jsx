import React from 'react'
import {reaction} from 'mobx'
import {Circle} from 'react-konva'


class Intersection extends React.Component {
	disposer;
	intersection;

	getColor(percent) {

	}

	render() {
		const {x, y} = this.props.intersection;

		return (
			<Circle x={x} y={y} radius={5} fill="purple"/>
		)
	}
}

export default Intersection