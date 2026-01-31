
document.addEventListener('DOMContentLoaded', () => {

    // Elements
    const palletRowsContainer = document.getElementById('pallet-rows');
    const addPalletBtn = document.getElementById('add-pallet-btn');
    const calculateBtn = document.getElementById('calculate-btn');
    const resetBtn = document.getElementById('reset-btn');
    const unitToggle = document.getElementById('unit-toggle'); // checkbox: checked = metric, unchecked = imperial
    const resultsPanel = document.getElementById('results-panel');
    const resultClass = document.getElementById('res-class');
    const resultDensity = document.getElementById('res-density');
    const resultVolume = document.getElementById('res-volume');
    const resultWeight = document.getElementById('res-weight');
    const printBtn = document.getElementById('print-btn');

    // State
    let isMetric = false;

    // init
    addPalletRow(); // Add first row by default

    // Event Listeners
    addPalletBtn.addEventListener('click', addPalletRow);

    if (printBtn) {
        printBtn.addEventListener('click', () => {
            window.print();
        });
    }

    // Toggle Unit
    unitToggle.addEventListener('change', (e) => {
        isMetric = e.target.checked;
        updateLabels();
        resetCalculator(false); // keep rows, just clear values? or convert? For now clear to be safe
    });

    calculateBtn.addEventListener('click', calculateFreightClass);

    resetBtn.addEventListener('click', () => {
        resetCalculator(true);
    });

    function addPalletRow() {
        const rowId = 'row-' + Date.now();
        const rowDiv = document.createElement('div');
        rowDiv.classList.add('pallet-row');
        rowDiv.id = rowId;

        // Dynamic labels based on IsMetric state
        const dimUnit = isMetric ? 'cm' : 'in';
        const weightUnit = isMetric ? 'kg' : 'lbs';

        const wrapper = document.createElement('div');
        wrapper.classList.add('row-inputs-wrapper');

        const dimInputs = document.createElement('div');
        dimInputs.classList.add('dimensions-inputs');

        const createInput = (id, labelText) => {
            const group = document.createElement('div');
            group.classList.add('input-group');
            const label = document.createElement('label');
            label.setAttribute('for', id);
            label.textContent = labelText;
            const input = document.createElement('input');
            input.type = 'number';
            input.min = '0';
            input.step = '0.1';
            input.id = id;
            input.required = true;
            group.appendChild(label);
            group.appendChild(input);
            return { group, input };
        };

        const lEntry = createInput(`${rowId}-l`, `Length (${dimUnit})`);
        lEntry.input.classList.add('dim-l');
        const wEntry = createInput(`${rowId}-w`, `Width (${dimUnit})`);
        wEntry.input.classList.add('dim-w');
        const hEntry = createInput(`${rowId}-h`, `Height (${dimUnit})`);
        hEntry.input.classList.add('dim-h');

        dimInputs.appendChild(lEntry.group);
        dimInputs.appendChild(wEntry.group);
        dimInputs.appendChild(hEntry.group);

        const weightInputs = document.createElement('div');
        weightInputs.classList.add('weight-inputs');

        const weightEntry = createInput(`${rowId}-weight`, `Weight (${weightUnit})`);
        weightEntry.input.classList.add('weight');
        const countEntry = createInput(`${rowId}-count`, `Count`);
        countEntry.input.classList.add('count');
        countEntry.input.step = '1';
        countEntry.input.value = '1';

        weightInputs.appendChild(weightEntry.group);
        weightInputs.appendChild(countEntry.group);

        wrapper.appendChild(dimInputs);
        wrapper.appendChild(weightInputs);

        const removeBtn = document.createElement('button');
        removeBtn.type = 'button';
        removeBtn.classList.add('row-remove-btn');
        removeBtn.innerHTML = '&times;'; // HTML entity is fine for static text
        removeBtn.title = 'Remove Row';
        removeBtn.setAttribute('aria-label', 'Remove Row');
        removeBtn.onclick = () => rowDiv.remove();

        rowDiv.appendChild(wrapper);
        rowDiv.appendChild(removeBtn);

        palletRowsContainer.appendChild(rowDiv);
    }

    function updateLabels() {
        const dimUnit = isMetric ? 'cm' : 'in';
        const weightUnit = isMetric ? 'kg' : 'lbs';

        // Update all existing labels
        document.querySelectorAll('.pallet-row').forEach(row => {
            const labels = row.querySelectorAll('label');
            // This relies on order, a bit brittle but simple. 
            // 0:L, 1:W, 2:H, 3:Weight, 4:Count
            if (labels[0]) labels[0].textContent = `Length (${dimUnit})`;
            if (labels[1]) labels[1].textContent = `Width (${dimUnit})`;
            if (labels[2]) labels[2].textContent = `Height (${dimUnit})`;
            if (labels[3]) labels[3].textContent = `Weight (${weightUnit})`;
        });
    }

    function resetCalculator(clearRows) {
        if (clearRows) {
            palletRowsContainer.innerHTML = '';
            addPalletRow();
        } else {
            // Just clear inputs
            document.querySelectorAll('input[type="number"]').forEach(inpt => inpt.value = '');
        }
        resultsPanel.classList.add('hidden');
    }

    function calculateFreightClass() {
        // Gather data
        const rows = document.querySelectorAll('.pallet-row');
        let totalVolumeCubicFeet = 0;
        let totalWeightLbs = 0;

        let hasError = false;

        rows.forEach(row => {
            let l = parseFloat(row.querySelector('.dim-l').value) || 0;
            let w = parseFloat(row.querySelector('.dim-w').value) || 0;
            let h = parseFloat(row.querySelector('.dim-h').value) || 0;
            let weight = parseFloat(row.querySelector('.weight').value) || 0;
            let count = parseFloat(row.querySelector('.count').value) || 1;

            if (l === 0 || w === 0 || h === 0 || weight === 0) {
                // If any value is 0/empty and it's a valid row, we might want to alert?
                // For now, treat as 0 and it won't add to totals, but logic dictates density will be inf or other issues.
                // We'll just continue; density checks will handle 0 volume.
            }

            // Convert to Imperial for Standardization
            if (isMetric) {
                // cm to inches
                l = l * 0.393701;
                w = w * 0.393701;
                h = h * 0.393701;
                // kg to lbs
                weight = weight * 2.20462;
            }

            // Calc Volume per piece in Cubic Feet
            // L*W*H (inches) / 1728
            const volPerPiece = (l * w * h) / 1728;

            totalVolumeCubicFeet += (volPerPiece * count);
            totalWeightLbs += (weight * count);
        });

        if (totalVolumeCubicFeet === 0) {
            alert("Please enter valid dimensions > 0");
            return;
        }

        // Density = Weight (lbs) / Volume (cu ft)
        const density = totalWeightLbs / totalVolumeCubicFeet;

        // Determine Class
        const fClass = getFreightClass(density);

        // Display
        resultVolume.textContent = totalVolumeCubicFeet.toFixed(2);
        resultWeight.textContent = totalWeightLbs.toFixed(2);
        resultDensity.textContent = density.toFixed(2);
        resultClass.textContent = fClass;

        resultsPanel.classList.remove('hidden');

        // Scroll to results
        resultsPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function getFreightClass(pcf) {
        if (pcf < 1) return "500";
        if (pcf < 2) return "400";
        if (pcf < 3) return "300";
        if (pcf < 4) return "250";
        if (pcf < 5) return "200";
        if (pcf < 6) return "175";
        if (pcf < 7) return "150";
        if (pcf < 8) return "125";
        if (pcf < 9) return "110";
        if (pcf < 10.5) return "100";
        if (pcf < 12) return "92.5";
        if (pcf < 13.5) return "85";
        if (pcf < 15) return "77.5";
        if (pcf < 22.5) return "70";
        if (pcf < 30) return "65";
        if (pcf < 35) return "60";
        if (pcf < 50) return "55";
        return "50";
    }

});
