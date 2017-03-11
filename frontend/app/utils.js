import Color from 'color'


const green = Color('#76FF03').hsl().object();
const red = Color('#FF3D00').hsl().object();
const delta = {
	h: red.h - green.h,
	s: red.s - green.s,
	l: red.l - green.l
};

export function getColor(percent) {
	return Color({
		h: green.h + percent*delta.h,
		s: green.s + percent*delta.s,
		l: green.l + percent*delta.l
	}).string()
}