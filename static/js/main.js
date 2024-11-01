gsap.from(".card1", {
    opacity:0,
    x : -1200,
    y : 200,
    ease: "power4.out",
    scrollTrigger:{
        trigger:".card1",
        scroller :"body", 
        // markers: true,
        start: "top 70%",
        end: "top 50%",
        scrub:3,
        // pin:true
    }
})

gsap.from(".card2", {
    opacity:0,
    x : 1200,
    y : 200,
    ease: "power4.out",
    scrollTrigger:{
        trigger:".card2",
        scroller :"body", 
        // markers: true,
        start: "top 70%",
        end: "top 50%",
        scrub:3,
        // pin:true
    }
})

gsap.from("#red", {
    opacity:0,
    scale : 0.4,
    ease: "power4.out",
    scrollTrigger:{
        trigger:"#red",
        scroller :"body", 
        // markers: true,
        start: "top 80%",
        end: "top 30%",
        scrub:4,
        // pin:true
    }

})