const tl = gsap.timeline()


tl.to(".animate-block-1",{
    // opacity:0,
    delay:0.8,
    x : 2000,
    duration:8,
    ease: "power3.out"
}, 0)

 .to(".animate-block-2",{
    // opacity:0,
    delay:0.8,
    x : -2000,
    duration:8,
    ease: "power3.out"
}, 0);



tl.from(".hero-section",{
    delay:1.6,
    opacity:0,
    y : 200,
    duration:1,
    ease: "power2.out"
}, 1);

gsap.from(".card1", {
    opacity:0,
    x : -1200,
    y : 200,
    ease: "power3.out",
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
    ease: "power3.out",
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
    ease: "power2.out",
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