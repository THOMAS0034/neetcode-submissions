class MinStack {
    constructor() {
        this.stack = [];
        this.min=[]
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val)
        
        if((this.min.length === 0 ) || (this.min[this.min.length -1] >= val )){
            this.min.push(val);
        }
    }

    /**
     * @return {void}
     */
    pop() {
        const pop = this.stack.pop();
        if(pop === this.min[this.min.length -1]){
            this.min.pop();
        }
    }

    /**
     * @return {number}
     */
    top() {
        const val = this.stack[this.stack.length - 1];
        return val;
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.min[this.min.length - 1];
    }
}
