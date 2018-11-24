
dpl ?= deploy.env
include $(dpl)
export $(shell sed 's/=.*//' $(dpl))

build:
	docker image build -t $(APP_NAME) .

run:
	docker container run --name $(APP_NAME) $(APP_NAME)

stop:
	docker container stop $(APP_NAME); docker container rm $(APP_NAME)

clean:
	docker container rm $(APP_NAME)

publish: tag-latest push-latest

tag-latest:
	docker tag $(APP_NAME):latest $(DOCKER_REPO)/$(APP_NAME):latest

push-latest:
	docker push $(DOCKER_REPO)