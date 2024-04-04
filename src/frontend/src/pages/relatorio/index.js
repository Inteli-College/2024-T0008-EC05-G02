import jsPDF from 'jspdf';

const doc = new jsPDF({
	orientation: 'landscape',
	unit: 'in',
	format: [4, 2],
});